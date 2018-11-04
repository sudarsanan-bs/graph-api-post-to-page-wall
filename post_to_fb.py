#!/usr/bin/python
import facebook
import datetime
import logging
import traceback
import os.path
import json

try:
        logging.basicConfig(filename='\PATH\TO\post_to_fb.log', level=logging.INFO)

        json_dict=[]
        
        #Open config_params.json in read mode
        with open('\PATH\TO\config_params.json','r') as input_file:
            logging.info("Parsing config file")
            input_json_string=input_file.read().replace('\n','')
            json_dict=json.loads(input_json_string) #Saving into a dictionary

        photo=open('\PATH\TO\photo.jpg','rb') #Read the photo to be posted (in binary mode)
        
        #Authenticate GraphAPI access using the 'page-access token' for the page
        graph=facebook.GraphAPI(access_token=json_dict['fb_access_token'],version='2.10')
        
        #Upload the photo and caption to create a new Facebook post into the page; in the process, retrieve the post ID for future reference
        graph_output_post_id=graph.put_photo(image=photo,album_path=json_dict['fb_page_id']+'/photos',message=json_dict['caption_for_your_post'])['id']
        #Cosntruct the share link for this post
        fb_share_link="https://facebook.com/"+json_dict['fb_page_id']+"/photos/a."+json_dict['fb_album_id']+"."+json_dict['fb_page_id']+"/%d/"%(int(graph_output_post_id))

        logging.info("The post has been successfully made. Use the following link to share it with your friends: "+fb_share_link)

except:
        logging.info("ERROR")
        logging.info(traceback.format_exc())
finally:
        logging.info(datetime.datetime.utcnow())
