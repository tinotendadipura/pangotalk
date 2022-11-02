from rest_framework import serializers
from  app. models import (ProductListing,ProductListingImages,BusinessProfile,Customer,BusinessBranch,
ProductCategory,Order,Event,EventBooking,Coupon,CouponClaim,InvoiceGenerator,KnoledgeBase,BannerImage,Feedback)
from chat. models import ChatMessage,Navigator,ListNavigator




class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = [
            'id',
            'customer_ID',
            'business_ID',   
            'message_ID',    
            'supportAgent',  
            'userName',      
            'country',       
            'message',       
            'phone',        
            'dateadded',        
            'supportMessage',   
            'message_is_opened', 
        ]



class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = [
            'business_ID',
            'customer_ID',
            'customerName',
            'phoneNumber',
            'feedback',
            'dateadded',
        ]





class KnoledgeBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnoledgeBase
        fields = [
            'id',
                     
            'tittle',             
            'description',     
            'mediafile',      
            'author',            
            'category',         
        ]


class BusinessBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessBranch
        fields = [
            'id',
            'business_ID',
            'branch_name', 
            'branch_ID',      
            'branch_city',      
            'branch_adress',       
            'branch_phone',        
            'longitude',          
            'latitude',  
        ]

class CouponClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponClaim
        fields = [
            'id',
            'business_ID',
            'campaignName',
            'couponCode',
            'percentage',
            'category',
            'minimum_amount',
            'claim_Name',
            'claim_Number',
            'claimed_on',
        ]



class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = [
            'id',
            'campaignBanner',   
            'campaignName',       
            'couponCode',         
            'percentage',         
            'Usage_limit',      
            'category',          
            'minimum_amount',   
            'startfulldate',     
            'startactualdate',    
            'startTime',        
            'endfullDate',      
            'endactuallDate', 
            'startTime',          
            'endTime',           
        ]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'business_ID',        
            'event_ID',           
            'event_Name',       
            'event_Description', 
            'eventimage',         
            'image_status',      
            'online_event',     
            'startfulldate',    
            'startactualdate',   
            'startTime',        
            'endfullDate',       
            'endactuallDate',    
            'startTime',         
            'endTime',           
        ]






class EventBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventBooking
        fields = [
            'id',
            'business_ID',      
            'customer_ID',        
            'booking_ID',      
            'event_ID',          
            'customerName',     
            'phone_Number',     
            'eventTittle',       
            'date',           
            'eventType',        
            'dateadded',           
        ]




class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
           'business_ID',
           'current_branch_status',
           'customer_name_status',
            'customerName',
            'App_User_Name',
            'location',
            'country',
            'code',
            'phone',
            'dateadded',
        ]





class NavigatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navigator
        fields = [
            'current_page',
            'phone',
            'dateadded',
        ]



class ListNavigatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListNavigator
        fields = [
            'current_item',
            'phone',
            'dateadded',
        ]



class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = [
            'business_ID',       
            'category',         
            'description',       
        ]



class ProductListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductListing
        fields = [
     'id',
    'business_ID', 
    'product_ID',    
    'title',         
    'product_image',  
    'description',   
    'category',        
    'price',          
    'currency',     
    'compare_price',  ]






class ProductListingImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductListingImages
        fields = [
    'profile_account_ID' ,'listingID' ,'productimage' ,        

    ]


class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = [
            'business_ID',
    'BusinessName',
    'logo_image',
    'Business_adress',
    'street_name', 
    'email',       
    'city',        
    'facebook',    
    'website',     
    'phone',       
    'banner_image',
    'other_phone',
    'longitude',   
    'latitude', 
    'form_completed',        

    ]





class BusinessBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = [
            'business_ID',
            'BusinessName',
            'banner_image'
           

    ]



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'business_ID',
            'product_image_url',
            'product_ID',
            'order_ID',
            'customerName',
            'customer_ID',
            'Payment_Method',
            'total_Amount',
            'payment_Status',
            'product_title',     
            'product_description',
            'orderQuantity',
            'phone',
            'country',
            'dateadded',   

    ]




class InvoiceGeneratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceGenerator
        fields = [
            'business_ID',       
            'invoice_file',     
            'order_ID',        
            'phone',  
        ]
