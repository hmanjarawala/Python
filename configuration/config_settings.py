# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 13:43:04 2020

@author: Himanshu.Manjarawala
"""

from baseclasses import ConfigurationSettings

class myConfigurationSettings(ConfigurationSettings):
    
    def get_settings(self) -> dict:
        data = {
                  "default": {
                    "profile_name": "Profile",
                    "player_name": "Player",
                    "profile_created": "1979-05-27T15:32:00.000Z",
                    "sound": "true"
                  },
                  "user": {
                    "profile": {
                      "name": "profile1",
                      "player_name": "player1",
                      "class": "warrior"
                    },
                    "settings": {
                      "sound": "false"
                    }
                  },
                  "default_inventory": {
                    "warrior": [
                      [
                        "sword",
                        "shield"
                      ],
                      [
                        "plate armor",
                        "plate helm"
                      ]
                    ],
                    "mage": [
                      [
                        "staff",
                        "wand"
                      ],
                      [
                        "robe",
                        "hood"
                      ]
                    ],
                    "items": [
                      "health potion",
                      "antidote",
                      "mana potion"
                    ]
                  }
            }
        return data