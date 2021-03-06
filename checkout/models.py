# coding=utf-8

from django.db import models
from django.conf import settings

from catalog.models import Book

class CartItemManager(models.Manager):

    def add_item(self, cart_key, book):
        if self.filter(cart_key=cart_key, book=book).exists():
            created = False
            cart_item = self.get(cart_key=cart_key, book=book)
            cart_item.quantity = cart_item.quantity + 1
            cart_item.save()
        else:
            created = True
            cart_item = CartItem.objects.create(
                cart_key=cart_key, book=book, price=book.price
            )
        return cart_item, created


class CartItem(models.Model):

    cart_key = models.CharField(
        'Chave do Carrinho', max_length=40, db_index=True
    )
    book = models.ForeignKey('catalog.Book', on_delete=models.CASCADE, verbose_name='Livro')
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    objects = CartItemManager()

    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens dos Carrinhos'
        unique_together = (('cart_key', 'book'),)

    def __str__(self):
        return '{} [{}]'.format(self.book, self.quantity)


class OrderManager(models.Manager):

    def create_order(self, user, cart_items):
        order = self.create(user=user)
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(
                order=order, quantity=cart_item.quantity, book=cart_item.book,
                price=cart_item.price
            )
        return order


class Order(models.Model):

    STATUS_CHOICES = (
        (0, 'Concluída'),
        (1, 'Aguardando Pagamento'),
        (2, 'Cancelada'),
    )

    PAYMENT_OPTION_CHOICES = (
        ('deposit', 'Depósito'),
        ('paypal', 'Paypal'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuário')
    status = models.IntegerField(
        'Situação', choices=STATUS_CHOICES, default=0, blank=True
    )
    payment_option = models.CharField(
        'Opção de Pagamento', choices=PAYMENT_OPTION_CHOICES, max_length=20,
        default='deposit'
    )

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    objects = OrderManager()

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return 'Pedido #{}'.format(self.pk)

    def books(self):
        books_ids = self.items.values_list('book')
        return Book.objects.filter(pk__in=books_ids)

    def total(self):
        aggregate_queryset = self.items.aggregate(
            total=models.Sum(
                models.F('price') * models.F('quantity'),
                output_field=models.DecimalField()
            )
        )
        return aggregate_queryset['total']

    def complete(self):
        self.status = 1
        self.save()

    def paypal(self):
        self.payment_option = 'paypal'
        self.save()
        paypal_dict = {
            'upload': '1',
            'business': settings.PAYPAL_EMAIL,
            'invoice': self.pk,
            'cmd': '_cart',
            'currency_code': 'BRL',
            'charset': 'utf-8',
        }
        index = 1
        for item in self.items.all():
            paypal_dict['amount_{}'.format(index)] = '%.2f' % item.price
            paypal_dict['item_name_{}'.format(index)] = item.book.name
            paypal_dict['quantity_{}'.format(index)] = item.quantity
            index = index + 1
        return paypal_dict


class OrderItem(models.Model):

    order = models.ForeignKey(Order, verbose_name='Pedido', on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey('catalog.Book', on_delete=models.CASCADE, verbose_name='Livro')
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens dos pedidos'

    def __str__(self):
        return '[{}] {}'.format(self.order, self.book)


def post_save_cart_item(instance, **kwargs):
    if instance.quantity < 1:
        instance.delete()


models.signals.post_save.connect(
    post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item'
)