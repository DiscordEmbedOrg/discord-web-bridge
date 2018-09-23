<template>
  <div id="app">
    <div class="wrapper">
      <div id="top" :style="getBackgroundColor">
        <GithubCorner :discordcolor="colors.discordfill" :discordfill="colors.discordcolor"/>
        <DiscordCorner :background="background" :discordEyes="discordEyes" customLink="https://discord.gg/Dkg79tc" :isRainbow="isRainbow" :animationStyle="animationStyle" id="discordcorner" :discordcolor="colors.discordfill" :discordfill="colors.discordcolor"/>
        <Intro/>
        <DiscordText :background="background" :discordEyes="discordEyes" :isRainbow="isRainbow" :animationStyle="animationStyle" ref="discordtext" :standardText="standardText" :discordfill="colors.discordfill" :discordcolor="colors.discordcolor" />
      </div>
      <MainBody id="mainbody" />
    </div>
  </div>
</template>

<script>
import Intro from './components/Intro.vue'
import DiscordCorner from './components/DiscordCorner.vue'
import GithubCorner from './components/GithubCorner.vue'
import MainBody from './components/MainBody.vue'
import DiscordText from './components/DiscordText.vue'

export default {
  name: 'App',
  components: {
    Intro, DiscordCorner, GithubCorner, MainBody, DiscordText
  },
  data () {
    return {
      background: 'none',
      discordEyes: 'none',
      isRainbow: false,
      animationStyle: 'swirl',
      standardText: "",
      previewDiscordType: 'standard',
      colors: {
        discordcolor: '#FFFFFF',
        discordfill: '#7289DA'
      }
    }
  },
  computed: {
    getBackgroundColor: {
      get: function() {
        return {
          backgroundColor: this.colors.discordfill,
          paddingBottom: "50px"
        }
      }
    }
  },
  methods: {
    updateSpeechBubble: function () {
      var myArray = ["This is the web client to discord-web-bridge (ง°ل͜°)ง",
                     "Built with ♥ by NNTin ≧◡≦",
                     "Hold on. This UI... Isn't this the Discord Client? 乁ʕ •̀ ۝ •́ ʔㄏ",
                     "ԅ[ •́ ﹏├┬┴┬┴ Fork me and create a more minimalistic looking client!",
                     "Message history is enabled on a select few channels (-_-｡)",
                     "Suggestions, Bugs? Contact me on Discordc (ˊᗜˋ*c)"];
      var rand = myArray[Math.floor(Math.random() * myArray.length)];
      this.standardText = rand;
    }
  },
  created: function () {
    this.updateSpeechBubble()
  }
}
</script>

<style>
html,body {
  height: 100%;
  width: 100%;
  margin: 0px;
  /*background-color: #2C2F33;*/
}
.wrapper {
  display: flex;
  height: 100%;
  flex-direction: column;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fff;
  height: 100%;
}
#top {
  flex: 0;
  height: 120px;
}
#mainbody {
  flex: 1;
  height: 100%;
}
#discordcorner {
	position: absolute;
	top: 0;
	left: 0;
	border: 0;
}
</style>
