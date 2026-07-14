from rest_framework import serializers
from products.models import ProductVariant
from orders.models import Order, OrderItem
from accounts.models import User


class DashboardOrderSerializer(serializers.ModelSerializer):

    customer = serializers.CharField(
        source="user.email"
    )

    class Meta:

        model = Order

        fields = (

            "order_number",

            "customer",

            "status",

            "total",

            "created_at",

        )

class LowStockSerializer(serializers.ModelSerializer):

    product = serializers.CharField(
        source="product.name"
    )

    color = serializers.CharField(
        source="color.name"
    )

    size = serializers.CharField(
        source="size.name"
    )

    class Meta:

        model = ProductVariant

        fields = (

            "sku",

            "product",

            "color",

            "size",

            "stock",

        )

class TopProductSerializer(serializers.ModelSerializer):

    product = serializers.CharField(
        source="product.name"
    )

    class Meta:

        model = OrderItem

        fields = (

            "product",

            "units_sold",

            "revenue",

        )

class DashboardCustomerSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = (

            "id",

            "first_name",

            "last_name",

            "email",

            "date_joined",

        )