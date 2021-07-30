<template>
  <router-view/>
</template>

<style>
@font-face {
  font-family: "inter";
  src: local("inter"),
    url(./assets/font/Inter-Regular.ttf) format("truetype");
}

@font-face {
  font-family: "inter-extrabold";
  src: local("inter-extrabold"),
    url(./assets/font/Inter-ExtraBold.ttf) format("truetype");
}

body,
html{
  font-family: 'inter';
  font-size: 16px;
  color: rgb(27, 27, 27);
  margin: 0px;
  padding: 0px;
}
</style>
