<template>
  <router-view/>
</template>

<style>
@font-face {
  font-family: "inter";
  src: local("inter"),
    url(./assets/font/Inter-Regular.ttf) format("truetype");
}

html {
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

body {
  font-family: 'inter';
  font-size: 16px;
  color: rgb(27, 27, 27);
  margin: 0;
}
</style>
