from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from agora_token_builder import RtcTokenBuilder
from .models import Post
from .serializers import PostSerializer

def register(request):
    return render(request, 'login.html')

def public_feed(request):
    posts = Post.objects.all().order_by('-created')
    context = {'posts': posts}
    return render(request, 'feed.html', context)


@api_view(['POST'])
def add_post(request):
    data = request.data
    post = Post.objects.create(sender= data['sender'], body=data['body'])
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


# @api_view(['POST'])
# def generate_token(request):
#     token = RtcTokenBuilder.buildToken(appId, appCertificate, userAccount, role, privilegeExpiredTs)