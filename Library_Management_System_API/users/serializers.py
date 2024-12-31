from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()



class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'date_of_membership','is_active']
        
        


    def update(self, instance, validated_data):
        # Ensure 'is_active' remains True even when updating other fields
        is_active = validated_data.get('is_active', instance.is_active)
        
        if not is_active:
            raise serializers.ValidationError("User cannot be inactive.")

        # Handle password hashing if it is being updated
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)

        # Update the user instance with the new data
        return super().update(instance, validated_data)    