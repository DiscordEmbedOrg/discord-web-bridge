<template>
  <div id="mainbody">
    <!--<div>{{ received_message }}</div>-->
    <div id="chat_window">
      <div id="chat_configuration">
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


<div class="theme-dark">
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
#mainbody {
  color: #000000;
}


.messagesWrapper-3lZDfY {
  height: 500px;
  width: 500px;
  text-align:start;
}



</style>
