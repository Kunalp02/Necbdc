from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages, auth
from newscatcherapi import NewsCatcherApiClient
from pprint import pprint

newscatcherapi = NewsCatcherApiClient(x_api_key='NiiydgX7I0jN9BRss-pKdJ5Hrx3Xfnr_UzCsCX9aRzA')


