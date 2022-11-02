from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    ProductListingAPIView,ProductListingImagesAPIView,BusinessProfileAPIView,
    ChatMessageCreateAPIView, NavigatorAPIView,CustomerCreateAPIView,UserPageUpdateAPIView,
    ListNavigatorAPIView,UserNavListUpdateAPIView,ProductCategoryAPIView,ProductListingDetailAPIView
    ,OrderCreateAPIView,AllProductAPIView,CustomerOrdersAPIView,AllEventsAPIView,EventDetailAPIView,
    BookEventAPIView,PromoAPIView,PromoDetailAPIView,ClaimCouponAPIView,MyCouponsAPIView,MyOrderDetailAPIView,
    GenerateOrderInvoiceAPIView, BranchAPIView, BranchListingDetailAPIView,KnoledgeBaseAPIView,ResoucesDetailAPIView,
    CustomerSignUpAPIView,CustomerNameUpdateAPIView,CustomerBranchUpdateAPIView,BusinessProfileDetailAPIView,FeedBackCreateAPIView
    
    
    )

urlpatterns = [
    path('nav/tracking', NavigatorAPIView.as_view()),
    path('nav/list-item',ListNavigatorAPIView.as_view()),
    path('signup/customer',CustomerSignUpAPIView.as_view()),
    path('signup/customer/add-user/name',CustomerNameUpdateAPIView.as_view()),
    path('signup/customer/add-user/branch',CustomerBranchUpdateAPIView.as_view()),
    path('product/category',ProductCategoryAPIView.as_view()),
    path('all/products',AllProductAPIView.as_view()),
    path('product/view/detail',ProductListingDetailAPIView.as_view()),
    
    
    path('product/order',OrderCreateAPIView.as_view()),
    path('customer/orders',CustomerOrdersAPIView.as_view()),
    path('my-order/details',MyOrderDetailAPIView.as_view()),
    path('my-order/generate-invoice',GenerateOrderInvoiceAPIView.as_view()),

    path('create/customer', CustomerCreateAPIView.as_view()),
    path('update/user/current_page', UserPageUpdateAPIView.as_view()),
    path('update/user/current_list_item', UserNavListUpdateAPIView.as_view()),
    path('chat/message', ChatMessageCreateAPIView.as_view()),
    path('customer/feedback', FeedBackCreateAPIView.as_view()),
    path('products', ProductListingAPIView.as_view()),
   
    path('all/all-promotions', PromoAPIView.as_view()),
    path('promo/coupon-details', PromoDetailAPIView.as_view()),
    path('promo/claim-coupon', ClaimCouponAPIView.as_view()),
    path('my-coupons', MyCouponsAPIView.as_view()),
   
    path('list/all-event', AllEventsAPIView.as_view()),
    path('event/details', EventDetailAPIView.as_view()),
    path('event/booking', BookEventAPIView.as_view()),
    path('products/media', ProductListingImagesAPIView.as_view()),
    path('business/details', BusinessProfileAPIView.as_view()),
    path('business/info/details', BusinessProfileDetailAPIView.as_view()),
    
    
    path('business/branchs',  BranchAPIView.as_view()),
    path('business/branchs/detail', BranchListingDetailAPIView.as_view()),
    
    path('business/knoledge-base', KnoledgeBaseAPIView.as_view()),
    path('resource/detail-info', ResoucesDetailAPIView.as_view()),

    
     
   
] 
