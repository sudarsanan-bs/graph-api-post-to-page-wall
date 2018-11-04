#!/usr/bin/python
import facebook
import datetime
import logging
import traceback
import os.path
import json

try:
        logging.basicConfig(filename='\PATH\TO\post_to_fb.log', level=logging.INFO)

        json_arr=[]

        ## config_params.json##
        #######################
        # {
        #     "fb_access_token": "EAACxxxxcBABlZBOYnSHxxxxxyyyyyyxxxxyyy2op2kfxXhmfbtiAMHFXBOkZCexxxxyyyyxyyx7kRYLnR1rYhg7JtTjn236cxJUO1bm2WJC7Vcxxxyyyyyyzzzzzzz91lqcNmDjEbhdAw8TlUZBT3Wo9jnsjndsd6asdjhXXXXX77777YYYYYYjewewek6YYYYYZZZZ",
        #     "caption_for_your_post": "Me and ma dawgs! 8)",
        #     "fb_page_id": "212345678910111",
        #     "fb_album_id": "012437922426691.0000000000"
        # }

        with open('\PATH\TO\config_params.json','r') as input_file:
            logging.info("Parsing config file")
            input_json_string=input_file.read().replace('\n','')
            json_arr=json.loads(input_json_string)

        fb_token = json_arr['fb_access_token']
        caption  = json_arr['caption_for_your_post']
        page_id  = json_arr['fb_page_id']
        album_id = json_arr['fb_album_id']

        photo=open('\PATH\TO\photo.jpg','rb')
        
        graph=facebook.GraphAPI(access_token=fb_token,version='2.10')

        graph_output_post_id=graph.put_photo(image=photo,album_path=page_id+'/photos',message=caption)['id']
        fb_share_link="https://facebook.com/"+page_id+"/photos/a."+album_id+"."+page_id+"/%d/"%(int(graph_output_post_id))

        logging.info("The post has been successfully made. Use the following link to share it with your friends: "+fb_share_link)

except:
        logging.info("ERROR")
        logging.info(traceback.format_exc())
finally:
        logging.info(datetime.datetime.utcnow())
