from django.db import models


class OfferBanner(models.Model):
    """A promotional banner placed in the mega menu or offer section."""

    PLACEMENT_MEGA_MENU = "mega_menu"
    PLACEMENT_OFFER_SECTION = "offer_section"

    PLACEMENT_CHOICES = (
        (PLACEMENT_MEGA_MENU, "Mega Menu Banner"),
        (PLACEMENT_OFFER_SECTION, "Offer Section Banner"),
    )

    title = models.CharField(
        max_length=200,
    )

    subtitle = models.CharField(
        max_length=300,
        blank=True,
    )

    placement_type = models.CharField(
        max_length=30,
        choices=PLACEMENT_CHOICES,
        default=PLACEMENT_MEGA_MENU,
    )

    image = models.ImageField(
        upload_to="cms/banners/",
        blank=True,
        null=True,
    )

    display_order = models.PositiveIntegerField(
        default=0,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ("display_order", "-created_at")

    def __str__(self):
        return self.title


class SiteBanner(models.Model):
    """
    A single, fixed-slot image used on the storefront (e.g. the
    Collection tile photos, the Sustainability banner). Unlike
    HeroSection/OfferBanner these aren't freely created and
    deleted — `key` is one of a known, hardcoded set that
    corresponds to a specific spot in the frontend layout. The
    admin only ever replaces the image for an existing slot.
    """

    KEY_COLLECTION_KURTI = "collection_kurti"
    KEY_COLLECTION_SHRUGS = "collection_shrugs"
    KEY_COLLECTION_SAREE = "collection_saree"
    KEY_COLLECTION_KAMEEZ = "collection_kameez"
    KEY_SUSTAINABILITY = "sustainability"

    KEY_HERO_SLIDE_1 = "hero_slide_1"
    KEY_HERO_SLIDE_2 = "hero_slide_2"
    KEY_HERO_SLIDE_3 = "hero_slide_3"

    # Same 3 hero slides, but a separate image slot each admins
    # can use to crop for phone screens instead of the desktop
    # photo getting awkwardly cropped by object-cover. Optional
    # — the storefront falls back to the desktop image on
    # mobile if these aren't set.
    KEY_HERO_SLIDE_1_MOBILE = "hero_slide_1_mobile"
    KEY_HERO_SLIDE_2_MOBILE = "hero_slide_2_mobile"
    KEY_HERO_SLIDE_3_MOBILE = "hero_slide_3_mobile"

    KEY_MODIWEEK_FEATURE = "modiweek_feature"

    KEY_SHOP_HERO = "shop_hero"
    KEY_SHOP_HERO_MOBILE = "shop_hero_mobile"

    KEY_SUSTAINABILITY_HERO = "sustainability_hero"
    KEY_SUSTAINABILITY_PROCESSING = "sustainability_processing"
    KEY_SUSTAINABILITY_MATERIALS = "sustainability_materials"
    KEY_SUSTAINABILITY_PACKAGING = "sustainability_packaging"
    KEY_SUSTAINABILITY_PRODUCT_CARING = (
        "sustainability_product_caring"
    )
    KEY_SUSTAINABILITY_TEAM_1 = "sustainability_team_1"
    KEY_SUSTAINABILITY_TEAM_2 = "sustainability_team_2"
    KEY_SUSTAINABILITY_TEAM_3 = "sustainability_team_3"
    KEY_SUSTAINABILITY_TEAM_4 = "sustainability_team_4"
    KEY_SUSTAINABILITY_TEAM_5 = "sustainability_team_5"
    KEY_SUSTAINABILITY_TEAM_6 = "sustainability_team_6"

    KEY_MEGAMENU_COLLECTION_1 = "megamenu_collection_1"
    KEY_MEGAMENU_COLLECTION_2 = "megamenu_collection_2"
    KEY_MEGAMENU_NEW_IN_1 = "megamenu_new_in_1"
    KEY_MEGAMENU_NEW_IN_2 = "megamenu_new_in_2"
    KEY_MEGAMENU_NEW_IN_3 = "megamenu_new_in_3"
    KEY_MEGAMENU_MODIWEEK_1 = "megamenu_modiweek_1"
    KEY_MEGAMENU_MODIWEEK_2 = "megamenu_modiweek_2"
    KEY_MEGAMENU_SUSTAINABILITY_1 = "megamenu_sustainability_1"
    KEY_MEGAMENU_SUSTAINABILITY_2 = "megamenu_sustainability_2"

    KEY_CHOICES = (
        (KEY_COLLECTION_KURTI, "Collection — Kurti"),
        (KEY_COLLECTION_SHRUGS, "Collection — Shrugs"),
        (KEY_COLLECTION_SAREE, "Collection — Saree"),
        (KEY_COLLECTION_KAMEEZ, "Collection — Kameez"),
        (KEY_SUSTAINABILITY, "Sustainability Banner"),
        (KEY_HERO_SLIDE_1, "Hero — Slide 1"),
        (KEY_HERO_SLIDE_2, "Hero — Slide 2"),
        (KEY_HERO_SLIDE_3, "Hero — Slide 3"),
        (KEY_HERO_SLIDE_1_MOBILE, "Hero — Slide 1 (Mobile)"),
        (KEY_HERO_SLIDE_2_MOBILE, "Hero — Slide 2 (Mobile)"),
        (KEY_HERO_SLIDE_3_MOBILE, "Hero — Slide 3 (Mobile)"),
        (KEY_MODIWEEK_FEATURE, "Modiweek — Feature Look"),
        (KEY_SHOP_HERO, "Shop All — Hero Banner"),
        (
            KEY_SHOP_HERO_MOBILE,
            "Shop All — Hero Banner (Mobile)",
        ),
        (
            KEY_SUSTAINABILITY_HERO,
            "Sustainability — Hero Image",
        ),
        (
            KEY_SUSTAINABILITY_PROCESSING,
            "Sustainability — Processing",
        ),
        (
            KEY_SUSTAINABILITY_MATERIALS,
            "Sustainability — Materials",
        ),
        (
            KEY_SUSTAINABILITY_PACKAGING,
            "Sustainability — Packaging",
        ),
        (
            KEY_SUSTAINABILITY_PRODUCT_CARING,
            "Sustainability — Product Caring",
        ),
        (
            KEY_SUSTAINABILITY_TEAM_1,
            "Sustainability — Team Photo 1",
        ),
        (
            KEY_SUSTAINABILITY_TEAM_2,
            "Sustainability — Team Photo 2",
        ),
        (
            KEY_SUSTAINABILITY_TEAM_3,
            "Sustainability — Team Photo 3",
        ),
        (
            KEY_SUSTAINABILITY_TEAM_4,
            "Sustainability — Team Photo 4",
        ),
        (
            KEY_SUSTAINABILITY_TEAM_5,
            "Sustainability — Team Photo 5",
        ),
        (
            KEY_SUSTAINABILITY_TEAM_6,
            "Sustainability — Team Photo 6",
        ),
        (
            KEY_MEGAMENU_COLLECTION_1,
            "Mega Menu — Collection Tile 1",
        ),
        (
            KEY_MEGAMENU_COLLECTION_2,
            "Mega Menu — Collection Tile 2",
        ),
        (
            KEY_MEGAMENU_NEW_IN_1,
            "Mega Menu — New In Tile 1",
        ),
        (
            KEY_MEGAMENU_NEW_IN_2,
            "Mega Menu — New In Tile 2",
        ),
        (
            KEY_MEGAMENU_NEW_IN_3,
            "Mega Menu — New In Tile 3",
        ),
        (
            KEY_MEGAMENU_MODIWEEK_1,
            "Mega Menu — Modiweek Tile 1",
        ),
        (
            KEY_MEGAMENU_MODIWEEK_2,
            "Mega Menu — Modiweek Tile 2",
        ),
        (
            KEY_MEGAMENU_SUSTAINABILITY_1,
            "Mega Menu — Sustainability Tile 1",
        ),
        (
            KEY_MEGAMENU_SUSTAINABILITY_2,
            "Mega Menu — Sustainability Tile 2",
        ),
    )

    key = models.CharField(
        max_length=50,
        choices=KEY_CHOICES,
        unique=True,
    )

    image = models.ImageField(
        upload_to="cms/site-banners/",
        blank=True,
        null=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ("key",)

    def __str__(self):
        return self.get_key_display()
