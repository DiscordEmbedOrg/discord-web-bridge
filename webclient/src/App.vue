<template>
  <div id="app">
    <div id="top" :style="getBackgroundColor">
      <GithubCorner :discordcolor="colors.discordfill" :discordfill="colors.discordcolor"/>
      <DiscordCorner :background="background" :discordEyes="discordEyes" customLink="https://discord.gg/Dkg79tc" :isRainbow="isRainbow" :animationStyle="animationStyle" id="discordcorner" :discordcolor="colors.discordfill" :discordfill="colors.discordcolor"/>
      <Intro/>
    </div>
    <MainBody/>
  </div>
</template>

<script>
import Intro from './components/Intro.vue'
import DiscordCorner from './components/DiscordCorner.vue'
import GithubCorner from './components/GithubCorner.vue'
import MainBody from './components/MainBody.vue'

export default {
  name: 'App',
  components: {
    Intro, DiscordCorner, GithubCorner, MainBody
  },
  data () {
    return {
      background: 'none',
      discordEyes: 'none',
      isRainbow: false,
      animationStyle: 'swirl',
      standardText: 'Join my Discord server!',
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
  }
}
</script>

<style>
html,body {
  height: 100%;
  margin: 0px;
  /*background-color: #2C2F33;*/
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #FFFFFF;
  height:100%
}
#discordcorner {
	position: absolute;
	top: 0;
	left: 0;
	border: 0;
}
</style>
