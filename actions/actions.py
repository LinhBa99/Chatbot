# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#

# Ham lay ket qua so xo va tra ve. Ten ham la action_get_lottery
#class action_get_lottery(Action):
#	def name(self):
            # Doan nay khai bao giong het ten ham ben tren la okie
#		    return 'action_get_lottery'
#	def run(self, dispatcher, tracker, domain):
            # Khai bao dia chi luu tru ket qua so xo. O day lam vi du nen minh lay ket qua SX Mien Bac
#            url = 'https://xskt.com.vn/rss-feed/mien-bac-xsmb.rss'
            # Tien hanh lay thong tin tu URL
#            feed_cnt = feedparser.parse(url)
            # Lay ket qua so xo moi nhat
#            first_node = feed_cnt['entries']
            # Lay thong tin ve ngay va chi tiet cac giai
#            return_msg = first_node[0]['title'] + "\n" + first_node[0]['description']
            # Tra ve cho nguoi dung
#            dispatcher.utter_message(return_msg)
#           return []

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_sdk import Action, Tracker
from typing import Text, List, Dict, Any

from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted
from rasa_sdk.executor import CollectingDispatcher
import requests
import json
import feedparser




class act_khuyen_mai(Action):

    def name(self) -> Text:
        return "act_khuyen_mai"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = {
            "text": "Những khách hàng đặc biệt có thẻ thành viên sẽ nhận được ưu đãi 10% khi mua hàng tại 5star",
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "làm thẻ",
                    "payload": "act_the",

                },
                {
                    "content_type": "text",
                    "title": "lợi ích thẻ",
                    "payload": "loi_the",

                },
            ]
        }
        dispatcher.utter_message(json_message=message)

        return []




class act_the(Action):

    def name(self) -> Text:
        return "act_the"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "phone_number",
            "title": "hotline",
            "payload": "0397648440"
        }

        button1 = {
            "type": "web_url",
            "url": "https://quantrimang.com/huong-dan-chon-size-giay-chuan-voi-moi-doi-chan-165577",
            "title": "Website"
        }
        button2 = {
            "type": "postback",
            "title": "Need more?",
            "payload": "more"
        }
        ret_text = "Hi! Để làm thẻ thành viên hãy chọn những cách sau đây:"
        dispatcher.utter_message(text=ret_text, buttons=[button, button1, button2])

        return []


class act_len(Action):

    def name(self) -> Text:
        return "act_len"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        shirt_list = []
        shirt0 = {
            "name": "Áo len nam",
            "image_url": "https://canifa.s3.amazonaws.com/media/catalog/product/8/t/8te20w019-se254-m.jpg",
            "intro": "199.000đ",
            "link": "https://canifa.com/catalog/product/view/id/221439/s/ao-len-nam-8TE20W019/category/99/",

        }
        shirt_list.append(shirt0)
        shirt1 = {
            "name": "Áo len  nam",
            "image_url": "https://canifa.s3.amazonaws.com/media/catalog/product/8/t/8te20w008-sa043-m.jpg",
            "intro": "299.000đ",
            "link": "https://canifa.com/catalog/product/view/id/221051/s/ao-len-nam-8te20w008/category/99/",

        }
        shirt_list.append(shirt1)
        shirt2 = {
            "name": "Áo len nam ",
            "image_url": "https://product.hstatic.net/1000341789/product/mausac_moss_dsc_3436__5__e33e56a028064932a5f1161c40a597a0_master.jpg",
            "intro": "199.000đ",
            "link": "https://routine.vn/products/ao-len-tay-dai-phoi-vai-form-regular-10f20kni008",

        }
        shirt_list.append(shirt2)


        template_items = []
        for shirt in shirt_list:

            template_item = {
                "title": shirt['name'],
                "image_url": shirt['image_url'],
                "subtitle": shirt['intro'],
                "default_action": {
                    "type": "web_url",
                    "url": shirt['link'],
                    "webview_height_ratio": "full"
                },
                "buttons": [
                    {
                        "type": "web_url",
                        "url": shirt['link'],
                        "title": "Xem ngay"
                    },
                    {
                        "type": "web_url",
                        "url": "https://canifa.com/skin/frontend/canifa/canifa-2019/images/sizechart/nam1.jpg",
                        "title": "size"
                    }
                ]
            }
            template_items.append(template_item)

        message_str = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": template_items

                }
            }
        }
        ret_text = "Hi! You can choose from below items:"
        print(message_str)
        dispatcher.utter_message(text=ret_text, json_message=message_str)

        return []