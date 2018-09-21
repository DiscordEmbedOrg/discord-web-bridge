<template>
  <div id="mainbody">
    <input type="text" v-model="message.user" placeholder="Your user name">
    <input type="text" v-model="message.user_avatar" placeholder="Avatar URL">
    <input type="text" v-model="message.content" placeholder="Content">
    <input type="text" v-model="message.channel_id" placeholder="Channel">
    <button v-on:click="send_message">Send</button>
    <div>{{ received_message }}</div>
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
      message: {
        user: "NNTin",
        user_avatar: "",
        content: "",
        channel_id: "398907517326852097"
      },
      received_message: null
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
      }
      console.log("Subscribing to topic.")
      session.subscribe("nntin.github.discord-web-bridge.message.398907517326852097", on_message);
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
          "author_name": this.message.user,
          "author_avatar_url": this.message.user_avatar,
          "content": this.message.content,
          "channel": this.message.channel_id
        }

        window.session.call("nntin.github.discord-web-bridge.rpc", [JSON.stringify(payload)]).then(
          function (res) {
            console.log("Result:", res);
          }
        )
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#mainbody {
  color: #000000
}

</style>
