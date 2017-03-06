from collections import OrderedDict

from rest_framework import serializers

from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):

    PUBLIC_FIELDS = ('uid')

    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'public', 'following', 'uid')


    def to_representation(self, obj):
        response = super(UserSerializer, self).to_representation(obj)

        remove = []
        
        if not obj.public:
            for field in response:
                if field not in self.PUBLIC_FIELDS:
                    remove.append(field)

        for i in remove:
            del response[i]
                    
        return response
