<template>
  <div class="wrapper">
    <div class="debug" style="display: none">
      <div>
        <input type="text" v-model="form_message.user" placeholder="Your user name">
        <input type="text" v-model="form_message.user_avatar" placeholder="Avatar URL">
        <input type="text" v-model="form_message.channel_id" placeholder="Channel">
        <button v-on:click="retrieve_history">retrieve history</button>
        <button v-on:click="test_method">test</button>
      </div>
      <div id="chat_send_message_box">
        <input type="text_method" v-model="form_message.content" placeholder="Content">
      </div>
    </div>
    <div class="discord-nntin-embed flex-1xMQg5 flex-1O1GKY horizontal-1ae9ci horizontal-2EEEnY flex-1O1GKY directionRow-3v3tfG justifyStart-2NDFzi alignStretch-DpGPf3 noWrap-3jynv6 spacer-29U_x8">
      <div class="channels-Ie2l6A vertical-V37hAW flex-1O1GKY directionColumn-35P_nr">
        <div class="flex-1xMQg5 flex-1O1GKY vertical-V37hAW flex-1O1GKY directionColumn-35P_nr justifyStart-2NDFzi alignStretch-DpGPf3 noWrap-3jynv6 container-PNkimc" style="flex: 1 1 auto;">
          <div class="flexChild-faoVW3" style="flex: 0 0 auto;">
            <div class="container-2Rl01u">
              <header class="header-2o-2hj">
                <span class="name-3YKhmS">test</span>
                <svg width="18" height="18" class="button-1w5pas">
                  <g fill="none" fill-rule="evenodd">
                    <path d="M0 0h18v18H0"></path>
                    <path stroke="#FFF" d="M4.5 4.5l9 9" stroke-linecap="round"></path>
                    <path stroke="#FFF" d="M13.5 4.5l-9 9" stroke-linecap="round"></path>
                  </g>
                </svg>
              </header>
            </div>
          </div>
          <div class="scrollerWrap-2lJEkd scrollerThemed-2oenus themeGhostHairlineChannels-3G0x9_ scrollerFade-1Ijw5y">
            <div class="scroller-2FKFPG scroller-2wx7Hm">
              <div style="width: 100%; height: 0px; visibility: hidden;"></div>
              <div class="container-0">
              <div style="height: 16px;"></div>
                <div class="containerDefault-1ZnADq" draggable="true">
                  <div tabindex="0" class="wrapperSelectedText-3dSUjC wrapper-KpKNwI" role="button">
                    <div class="contentSelectedText-3wUhMi content-20Aix8">
                      <div class="marginReset-3RfdVe" style="flex: 0 0 auto;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" class="colorSelectedText-1y4Wvs icon-sxakjD">
                          <path class="foreground-2W-aJk" fill="currentColor" d="M2.27333333,12 L2.74666667,9.33333333 L0.08,9.33333333 L0.313333333,8 L2.98,8 L3.68666667,4 L1.02,4 L1.25333333,2.66666667 L3.92,2.66666667 L4.39333333,0 L5.72666667,0 L5.25333333,2.66666667 L9.25333333,2.66666667 L9.72666667,0 L11.06,0 L10.5866667,2.66666667 L13.2533333,2.66666667 L13.02,4 L10.3533333,4 L9.64666667,8 L12.3133333,8 L12.08,9.33333333 L9.41333333,9.33333333 L8.94,12 L7.60666667,12 L8.08,9.33333333 L4.08,9.33333333 L3.60666667,12 L2.27333333,12 L2.27333333,12 Z M5.02,4 L4.31333333,8 L8.31333333,8 L9.02,4 L5.02,4 L5.02,4 Z" transform="translate(1.333 2)"></path>
                        </svg>
                      </div>
                      <div class="nameSelectedText-sp_EUw name-3M0b8v overflowEllipsis-jeThUf" style="flex: 1 1 auto;">aaa</div>
                    </div>
                  </div>
                </div>
                <div class="containerDefault-1ZnADq" draggable="true">
                  <div tabindex="0" class="wrapperDefaultText-2IWcE8 wrapper-KpKNwI" role="button">
                    <div class="contentDefaultText-3vZplL content-20Aix8">
                      <div class="marginReset-3RfdVe" style="flex: 0 0 auto;">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" class="colorDefaultText-oas-QM icon-sxakjD">
                          <path class="foreground-2W-aJk" fill="currentColor" d="M2.27333333,12 L2.74666667,9.33333333 L0.08,9.33333333 L0.313333333,8 L2.98,8 L3.68666667,4 L1.02,4 L1.25333333,2.66666667 L3.92,2.66666667 L4.39333333,0 L5.72666667,0 L5.25333333,2.66666667 L9.25333333,2.66666667 L9.72666667,0 L11.06,0 L10.5866667,2.66666667 L13.2533333,2.66666667 L13.02,4 L10.3533333,4 L9.64666667,8 L12.3133333,8 L12.08,9.33333333 L9.41333333,9.33333333 L8.94,12 L7.60666667,12 L8.08,9.33333333 L4.08,9.33333333 L3.60666667,12 L2.27333333,12 L2.27333333,12 Z M5.02,4 L4.31333333,8 L8.31333333,8 L9.02,4 L5.02,4 L5.02,4 Z" transform="translate(1.333 2)"></path>
                        </svg>
                      </div>
                      <div class="nameDefaultText-24KCy5 name-3M0b8v overflowEllipsis-jeThUf" style="flex: 1 1 auto;">bbb</div>
                    </div>
                  </div>
                </div>
              </div>
              <div style="width: 100%; height: 0px; visibility: hidden;"></div>
            </div>
          </div>
        </div>
        <div class="container-2Thooq">
          <div class="wrapper-2F3Zv8 small-5Os1Bb avatar-small">
            <div user="Linley" status="online" class="avatar-3JE4B3 avatar-small stop-animation" style="background-image: url(&quot;https://i.imgur.com/e4Gnvgw.png&quot;);"></div>
            <div class="online-2S838R status-oxiHuE small-5Os1Bb status status-2kJpnA"></div>
          </div>
          <div class="accountDetails-3k9g4n nameTag-m8r81H"><span class="username">Web</span><span class="discriminator">#8384</span></div>
          <div class="accountDetails-3k9g4n nameTag-m8r81H"><span class="username">{{ form_message.user }}</span></div>
        </div>
      </div>
      <div class="chat-3bRxxu">
        <div class="content-yTz4x3">
          <div class="flex-spacer flex-vertical">
            <div class="messagesWrapper-3lZDfY">
              <div class="scroller-wrap scrollerWrap-2su1QI">
                <div class="messages-3amgkR scroller" id="scroller">
                  <div v-for="message in messages">
                    <div class="containerCozyBounded-1rKFAn containerCozy-jafyvG container-1YxwTf">
                      <div class="messageCozy-2JPAPA message-1PNnaP">
                        <div class="headerCozy-2N9HOL">
                          <div class="wrapper-2F3Zv8 large-3ChYtB avatar-17mtNa" tabindex="-1">
                            <div class="image-33JSyf large-3ChYtB">
                              <img class="image-33JSyf large-3ChYtB" :src="message.user_avatar">
                            </div>
                          </div>
                          <h2 class="headerCozyMeta-rdohGq">
                            <span class="usernameWrapper-1S-G5O">{{ message.user }}</span>
                          </h2>
                          <time class="timestampCozy-2hLAPV" :datetime="message.created_at"></time>
                        </div>
                        <div class="contentCozy-3XX413 content-3dzVd8">
                          <div class="containerCozy-336-Cz container-206Blv">
                            <div class="markup-2BOw-j">{{ message.content }}</div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <form>
              <div class="channelTextArea-1LDbYG channelTextArea-rNsIhG">
                <div class="inner-zqa7da flex-1O1GKY innerNoAutocomplete-1WpcVO">
                  <!--<div class="flex-1xMQg5 flex-1O1GKY horizontal-1ae9ci horizontal-2EEEnY flex-1O1GKY directionRow-3v3tfG justifyStart-2NDFzi alignStretch-DpGPf3 noWrap-3jynv6" style="flex: 1 1 auto;">
                    <button tabindex="3" type="button" class="attachButton-1UjEWA button-38aScr lookBlank-3eh9lL colorBrand-3pXr91 grow-q77ONN">
                      <div class="contents-18-Yxp attachButtonInner-1iyZ9F">
                        <svg width="24" height="24" viewBox="0 0 24 24">
                          <path fill="currentColor" class="attachButtonPlus-rUdX-B" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm5 11h-4v4h-2v-4H7v-2h4V7h2v4h4v2z">
                          </path>
                        </svg>
                      </div>
                    </button>
                    <div class="attachButtonDivider-3Glu60">
                    </div>
                  </div>
                  <div class="uploadInput-2lNPSo">
                    <div class="file-input" style="position: absolute; top: 0px; left: 0px; width: 100%; height: 100%; opacity: 0; cursor: pointer;">
                    </div>
                  </div>-->
                  <textarea autofocus v-model="form_message.content" rows="1" @keyup.13.enter="send_message" placeholder="Message #aaa" tabindex="1" class="textArea-2Spzkt textArea-2Spzkt scrollbarGhostHairline-1mSOM1 scrollbar-3dvm_9" style="height: auto;" />
                  <!--<button tabindex="2" type="button" class="emojiButtonNormal-TdumYh emojiButton-3uL3Aw emojiButton-2wRZts button-38aScr lookBlank-3eh9lL colorBrand-3pXr91 grow-q77ONN">
                    <div class="contents-18-Yxp">
                      <div class="spriteNormal-1wvG5n sprite-2iCowe" style="background-position: 0px 0px; background-size: 242px 110px;">
                      </div>
                    </div>
                  </button>-->
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import json from '../config.json'
export default {
  name: 'MainBody',
  data () {
    return {
      myJson: json,
      session: null,
      test: null,
      form_message: {
        user: "NNTin",
        user_avatar: "",
        content: "",
        channel_id: "398907517326852097"
      },
      messages: [],
      received_message: {
        content: "",
        created_at: "",
        id: null,
        user: "",
        user_avatar: ""
      },
      subscription: null,
      usernames: ['Anti-Mage', 'Axe', 'Bane', 'Bloodseeker', 'Crystal Maiden',
        'Drow Ranger', 'Earthshaker', 'Juggernaut', 'Mirana', 'Shadow Fiend',
        'Morphling', 'Phantom Lancer', 'Puck', 'Pudge', 'Razor', 'Sand King',
        'Storm Spirit', 'Sven', 'Tiny', 'Vengeful Spirit', 'Windranger', 'Zeus',
        'Kunkka', 'Lina', 'Lich', 'Lion', 'Shadow Shaman', 'Slardar', 'Tidehunter',
        'Witch Doctor', 'Riki', 'Enigma', 'Tinker', 'Sniper', 'Necrophos', 'Warlock',
        'Beastmaster', 'Queen of Pain', 'Venomancer', 'Faceless Void', 'Wraith King',
        'Death Prophet', 'Phantom Assassin', 'Pugna', 'Templar Assassin', 'Viper',
        'Luna', 'Dragon Knight', 'Dazzle', 'Clockwerk', 'Leshrac', "Nature's Prophet",
        'Lifestealer', 'Dark Seer', 'Clinkz', 'Omniknight', 'Enchantress', 'Huskar',
        'Night Stalker', 'Broodmother', 'Bounty Hunter', 'Weaver', 'Jakiro', 'Batrider',
        'Chen', 'Spectre', 'Doom', 'Ancient Apparition', 'Ursa', 'Spirit Breaker',
        'Gyrocopter', 'Alchemist', 'Invoker', 'Silencer', 'Outworld Devourer', 'Lycan',
        'Brewmaster', 'Shadow Demon', 'Lone Druid', 'Chaos Knight', 'Meepo',
        'Treant Protector', 'Ogre Magi', 'Undying', 'Rubick', 'Disruptor',
        'Nyx Assassin', 'Naga Siren', 'Keeper of the Light', 'Io', 'Visage', 'Slark',
        'Medusa', 'Troll Warlord', 'Centaur Warrunner', 'Magnus', 'Timbersaw',
        'Bristleback', 'Tusk', 'Skywrath Mage', 'Abaddon', 'Elder Titan',
        'Legion Commander', 'Ember Spirit', 'Earth Spirit', 'Terrorblade', 'Phoenix', 
        'Oracle', 'Techies', 'Winter Wyvern', 'Arc Warden', 'Underlord', 'Monkey King',
        'Pangolier', 'Dark Willow', 'Grimstroke']
    }
  },
  created: function () {
    var index = Math.floor(Math.random() * this.usernames.length);
    this.form_message.user = this.usernames[index] + " " + Math.floor(Math.random() * 100000).toString()


    var connection = new autobahn.Connection({
      url: this.myJson.ws,
      realm: 'realm1'
    });
    var that = this

    connection.onopen = function (session) {
      window.session = session;
      console.log("Websocket is now open!")

      function on_message(args) {
        that.received_message = args[0]
        that.messages.push(args[0])
        //while (that.messages.length > 10) {
        //  that.messages.shift();
        //}
        console.log(that.received_message)

        that.$nextTick(function () {
          var scroller = document.getElementById("scroller");
          scroller.scrollTop = scroller.scrollHeight;
        });
      }
      console.log("Subscribing to topic.")
      session.subscribe("nntin.github.discord-web-bridge.message.398907517326852097", on_message).then(
        function (res) {
          that.subscription = res
          that.retrieve_history()
        }
      );

    };
    connection.open();

  },
  methods: {
    update: function() {
      console.log("hello")
    },
    send_message: function(event) {
      if(typeof window.session !== "undefined" && event.which == 13 && !event.shiftKey) {
        var payload = {
          "author_name": this.form_message.user,
          "author_avatar_url": this.form_message.user_avatar,
          "content": this.form_message.content,
          "channel": this.form_message.channel_id
        }

        window.session.call("nntin.github.discord-web-bridge.rpc", [JSON.stringify(payload)]).then(
          function (res) {
            console.log("Result:", res);
          }
        )
        this.form_message.content = "";
      }
    },
    retrieve_history: function() {
      var that = this
      if(typeof window.session !== "undefined") {
        window.session.call('wamp.subscription.get_events', [this.subscription.id, 20]).then(
          function (history) {
            console.log("got history for " + history.length + " events");
            //for (var i = 0; i < history.length; ++i) {
            for (var i = history.length - 1; i > -1; i--) {
              console.log(history[i].timestamp, history[i].publication, history[i].args[0]);
              that.messages.push(history[i].args[0]);
            }
            //that.messages = history;
            console.log(that.messages)

            that.$nextTick(function () {
              var scroller = document.getElementById("scroller");
              scroller.scrollTop = scroller.scrollHeight;
            });
          },
          function (err) {
            console.log("could not retrieve event history", err);
          }
        );
      }
    },
    test_method: function() {
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.wrapper {
  display: flex;
  height: 100%;
  flex-direction: column;
}

.debug {
  flex: 0;
}

.discord-nntin-embed {
  flex: 1;
  display:flex;
  text-align:start;
}

.chat-3bRxxu {
  background-color:rgb(54, 57, 63);
}

.channelTextArea-1LDbYG {
}

.inner-zqa7da {
  background-color:rgba(114, 118, 125, 0.298039);
}

.textArea-2Spzkt {
  color: #fff;
}


</style>
