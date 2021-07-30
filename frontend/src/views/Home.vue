<template>
  <div>
    <top-bar/>

    <div class="body">
      <span class="start-message">
        Integrate math with
        <br>
        Math<span class="api">API</span>
      </span>
      <span class="description-text">
        Solve function, get function points for a plot, get derivatives and integrals, solve problems with numerical methods and much more...
        <br><br>
        With Math<span class="api">API</span> integrating math to your proyects just became easy.
      </span>
    </div>

    <div class="body body-info">
      <span class="description-text">
        With Math<span class="api">API</span> yo can
      </span>

      <div class="feature-box">

      </div>
    </div>

  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import TopBar from '../components/TopBar.vue';

//import functionIcon from '../assets/icons/function.svg';

export default defineComponent({
  name: 'Home',
  components: { TopBar },
});
</script>

<style>
.body {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: calc(100vh - 80px);
}
.body-info {
  height: 100vh;
  justify-content: flex-start;
}
.start-message {
  width: 70%;
  text-align: center;
  font-family: inter-extrabold;
  font-size: 80px;
}
.api {
  color: rgb(59, 46, 131);
}
.description-text {
  width: 80%;
  margin-top: 30px;
  text-align: center;
  font-size: 20px;
  font-weight: 600;
  color: rgb(94, 94, 94);
}
.feature-box {
  width: 80%;
  display: flex;
  flex-wrap: wrap;
  height: 100%;
}
</style>