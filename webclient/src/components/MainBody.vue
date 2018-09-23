<template>
  <div class="wrapper">
    <div class="debug">
      <div>
        <input type="text" v-model="form_message.user" placeholder="Your user name">
        <input type="text" v-model="form_message.user_avatar" placeholder="Avatar URL">
        <input type="text" v-model="form_message.channel_id" placeholder="Channel">
        <button v-on:click="retrieve_history">retrieve history</button>
        <button v-on:click="test_method">test</button>
      </div>
      <div id="chat_send_message_box">
        <input type="text_method" v-model="form_message.content" placeholder="Content">
        <button v-on:click="send_message">Send</button>
      </div>
    </div>
    <div class="discord-nntin-embed flex-1xMQg5 flex-1O1GKY horizontal-1ae9ci horizontal-2EEEnY flex-1O1GKY directionRow-3v3tfG justifyStart-2NDFzi alignStretch-DpGPf3 noWrap-3jynv6 spacer-29U_x8">
      <div class="channels-Ie2l6A vertical-V37hAW flex-1O1GKY directionColumn-35P_nr">
        <div class="flex-1xMQg5 flex-1O1GKY vertical-V37hAW flex-1O1GKY directionColumn-35P_nr justifyStart-2NDFzi alignStretch-DpGPf3 noWrap-3jynv6 container-PNkimc">
          <div class="scrollerWrap-2lJEkd scrollerThemed-2oenus themeGhostHairlineChannels-3G0x9_ scrollerFade-1Ijw5y">
            <div class="scroller-2FKFPG scroller-2wx7Hm">
              <div class="container-0">
                <div v-for="message in messages">
                  <div class="containerDefault-1ZnADq">
                    <div class="wrapperDefaultText-2IWcE8 wrapper-KpKNwI" tabindex="0" role="button">
                      <div class="contentDefaultText-3vZplL content-20Aix8">
                        <div class="marginReset-3RfdVe" style="flex: 0 0 auto;">
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" class="colorDefaultText-oas-QM icon-sxakjD"><path class="foreground-2W-aJk" fill="currentColor" d="M2.27333333,12 L2.74666667,9.33333333 L0.08,9.33333333 L0.313333333,8 L2.98,8 L3.68666667,4 L1.02,4 L1.25333333,2.66666667 L3.92,2.66666667 L4.39333333,0 L5.72666667,0 L5.25333333,2.66666667 L9.25333333,2.66666667 L9.72666667,0 L11.06,0 L10.5866667,2.66666667 L13.2533333,2.66666667 L13.02,4 L10.3533333,4 L9.64666667,8 L12.3133333,8 L12.08,9.33333333 L9.41333333,9.33333333 L8.94,12 L7.60666667,12 L8.08,9.33333333 L4.08,9.33333333 L3.60666667,12 L2.27333333,12 L2.27333333,12 Z M5.02,4 L4.31333333,8 L8.31333333,8 L9.02,4 L5.02,4 L5.02,4 Z" transform="translate(1.333 2)"></path></svg>
                        </div>
                        <div class="nameDefaultText-24KCy5 name-3M0b8v overflowEllipsis-jeThUf" style="flex: 1 1 auto;">text channel</div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="container-2Thooq">
          <div class="wrapper-2F3Zv8 small-5Os1Bb avatar-small">
            <div user="Linley" status="online" class="avatar-3JE4B3 avatar-small stop-animation" style="background-image: url(&quot;https://i.imgur.com/e4Gnvgw.png&quot;);">
            </div>
            <div class="online-2S838R status-oxiHuE small-5Os1Bb status status-2kJpnA"></div>
          </div>
          <div class="accountDetails-3k9g4n nameTag-m8r81H">
            <span class="username">
              Web
            </span>
            <span class="discriminator">
              #8384
            </span>
          </div>
          <div class="accountDetails-3k9g4n nameTag-m8r81H">
            <span class="username">
              Linley
            </span>
            <span class="discriminator">
              #8686
            </span>
          </div>
        </div>
      </div>
      <div class="chat-3bRxxu">
        <div class="content-yTz4x3">
          <div class="flex-spacer flex-vertical">
            <div class="messagesWrapper-3lZDfY">
              <div class="scroller-wrap scrollerWrap-2su1QI">
                <div class="messages-3amgkR scroller">
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
                  <textarea v-model="form_message.content" rows="1" placeholder="Message #aaa" tabindex="1" class="textArea-2Spzkt textArea-2Spzkt scrollbarGhostHairline-1mSOM1 scrollbar-3dvm_9" style="height: auto;" />
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
      subscription: null
    }
  },
  created: function () {
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
    send_message: function() {
      if(typeof window.session !== "undefined") {
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
      }
      this.form_message.content = "";
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


</style>
