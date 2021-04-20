import redis
import json

r = redis.Redis(
host='redis-16948.c261.us-east-1-4.ec2.cloud.redislabs.com',
port="16948",
password='mKrF5q87X669hK30xkeJRPkI5WoeeoZt')

profile = json.dumps({
  "login":"",
  "Id":"",
  "name":"",
  "followers":[],
  "posts":[
    {
      "date":"",
      "data":""
      }
  ]
})
post = json.dumps({
  "date":"",
  "data":""
})
r.hset("hash", profile, post)
