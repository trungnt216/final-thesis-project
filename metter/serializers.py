from rest_framework import serializers
from metter.models import Metter

class MetterSerializer(serializers.ModelSerializer):
    class Meta:
      model = Metter
      fields = ('id','airms', 'birms', 
                'cirms', 'avrms', 'bvrms', 
                'cvrms', 'awatt', 'bwatt',
                  'cwatt', 'avar', 'bvar', 
                  'cvar', 'ava', 'bva', 'cva', 
                  'awatthr_hi', 'bwatthr_hi', 'cwatthr_hi', 
                  'created_at','index')
