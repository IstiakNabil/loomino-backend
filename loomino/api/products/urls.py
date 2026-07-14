from django.urls import path

from .views import (
    ProductListAPIView,
    ProductDetailAPIView,
    CategoryListAPIView,
    BrandListAPIView,
    FeaturedProductAPIView,
    NewArrivalProductAPIView,
    BestSellerProductAPIView,
    RelatedProductAPIView,
    ColorListAPIView,
    SizeListAPIView,
    ModiweekProductAPIView,
    AdminColorListCreateAPIView,
    AdminColorRetrieveUpdateDestroyAPIView,
    AdminProductListCreateAPIView,
    AdminProductRetrieveUpdateDestroyAPIView,
    AdminSizeListCreateAPIView,
    AdminSizeRetrieveUpdateDestroyAPIView,
    # Admin Categories
    AdminCategoryListCreateAPIView,
    AdminCategoryRetrieveUpdateDestroyAPIView,
    AdminProductVariantListCreateAPIView,
    AdminProductVariantRetrieveUpdateDestroyAPIView,
)


urlpatterns = [

    # ========================================================
    # Public Product Endpoints
    # ========================================================

    path(
        "",
        ProductListAPIView.as_view(),
        name="product-list",
    ),

    path(
        "featured/",
        FeaturedProductAPIView.as_view(),
        name="featured-products",
    ),

    path(
        "new-arrivals/",
        NewArrivalProductAPIView.as_view(),
        name="new-arrivals",
    ),

    path(
        "best-sellers/",
        BestSellerProductAPIView.as_view(),
        name="best-sellers",
    ),

    path(
        "modiweek/",
        ModiweekProductAPIView.as_view(),
        name="modiweek-products",
    ),

    path(
        "categories/",
        CategoryListAPIView.as_view(),
        name="category-list",
    ),

    path(
        "brands/",
        BrandListAPIView.as_view(),
        name="brand-list",
    ),

    path(
        "colors/",
        ColorListAPIView.as_view(),
        name="color-list",
    ),

    path(
        "sizes/",
        SizeListAPIView.as_view(),
        name="size-list",
    ),


    # ========================================================
    # Admin Product Endpoints
    # Keep these above the dynamic slug route
    # ========================================================

    path(
        "admin/",
        AdminProductListCreateAPIView.as_view(),
        name="admin-product-list-create",
    ),

    path(
        "admin/<int:pk>/",
        AdminProductRetrieveUpdateDestroyAPIView.as_view(),
        name="admin-product-detail",
    ),


        # ========================================================
    # Admin Category Endpoints
    # ========================================================

    path(
        "categories/manage/",
        AdminCategoryListCreateAPIView.as_view(),
        name="admin-category-list-create",
    ),

    path(
        "categories/manage/<int:pk>/",
        AdminCategoryRetrieveUpdateDestroyAPIView.as_view(),
        name="admin-category-detail",
    ),


        # ========================================================
    # Admin Color Endpoints
    # ========================================================

    path(
        "colors/manage/",
        AdminColorListCreateAPIView.as_view(),
        name="admin-color-list-create",
    ),

    path(
        "colors/manage/<int:pk>/",
        AdminColorRetrieveUpdateDestroyAPIView.as_view(),
        name="admin-color-detail",
    ),

        # ========================================================
    # Admin Size Endpoints
    # ========================================================

    path(
        "sizes/manage/",
        AdminSizeListCreateAPIView.as_view(),
        name="admin-size-list-create",
    ),

    path(
        "sizes/manage/<int:pk>/",
        AdminSizeRetrieveUpdateDestroyAPIView.as_view(),
        name="admin-size-detail",
    ),

        # ========================================================
    # Admin Product Variant Endpoints
    # ========================================================

    path(
        "variants/admin/",
        AdminProductVariantListCreateAPIView.as_view(),
        name="admin-product-variant-list-create",
    ),

    path(
        "variants/admin/<int:pk>/",
        AdminProductVariantRetrieveUpdateDestroyAPIView.as_view(),
        name="admin-product-variant-detail",
    ),
    # ========================================================
    # Dynamic Product Slug Endpoints
    # Keep these last
    # ========================================================

    path(
        "<slug:slug>/related/",
        RelatedProductAPIView.as_view(),
        name="related-products",
    ),

    path(
        "<slug:slug>/",
        ProductDetailAPIView.as_view(),
        name="product-detail",
    ),

]