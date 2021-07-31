<template>
  <div class="top-bar">

    <span @click="goHome" class="api-name">
      Math<span class="api">API</span>
    </span>

    <div class="page-buttons">
      <span @click="goToDocs" class="docs-button">Docs</span>
      <span @click="goToTryAPI" class="try-it-button">Try it</span>
    </div>

  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: "top-bar",
  methods: {
    goToDocs() {
      window.open('https://github.com/jralvarenga/mathapi');
    },
    goToTryAPI() {
      this.$router.push('/try-api');
    },
    goHome() {
      this.$router.push('/');
    }
  }
})
</script>

<style>
.top-bar {
  height: 80px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding-left: 5%;
  padding-right: 5%;
}
.api-name {
  font-size: 30px;
  font-weight: 800;
  cursor: pointer;
}
.api {
  color: rgb(59, 46, 131);
}
.page-buttons {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.try-it-button {
  padding: 10px;
  padding-left: 35px;
  padding-right: 35px;
  background: rgb(59, 46, 131);
  color: #fff;
  font-weight: 800;
  border-radius: 10px;
  cursor: pointer;
  transition: 300ms;
}
.try-it-button:hover {
  background: rgb(47, 37, 104);
  transition: 100ms;
}
.try-it-button:active {
  background: rgb(82, 65, 182);
}

.docs-button {
  margin-right: 30px;
  font-weight: bold;
  cursor: pointer;
  transition: 200ms;
}
.docs-button:hover {
  color: rgb(138, 138, 138);
}
</style>