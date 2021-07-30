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

      <div class="feature-container">

        <div class="feature-box" @click="goToDoc(feat.link)" v-for="feat, i in features" :key="i">
          <div class="feat-name">
            <span>{{ feat.name }}</span>
            <img class="feat-icon" :src="feat.icon" alt="">
          </div>
          <div class="feat-description">
            <span>{{ feat.description }}</span>
          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import TopBar from '../components/TopBar.vue';

//import functionIcon from '../assets/icons/function.svg';

interface AppFeatures {
  name: string
  icon: string
  description: string
}

export default defineComponent({
  name: 'Home',
  components: { TopBar },
  data() {
    return {
      features: [{
        name: 'Function Solver',
        description: "Solves function in any point given, gets plot points and gets function critic values",
        link: 'https://github.com/jralvarenga/mathapi/tree/master/mathapi/math/function',
        icon: 'icons/function.svg'
      },
      {
        name: 'Function Derivative',
        description: "Get function derivative and/or can evaluate derivatives in any point given",
        link: 'https://github.com/jralvarenga/mathapi/tree/master/mathapi/math/derivative',
        icon: 'icons/plot.svg'
      },
      {
        name: 'Function Integral',
        description: "Get function integral and/or can evaluate integral in any point given",
        link: 'https://github.com/jralvarenga/mathapi/tree/master/mathapi/math/integral',
        icon: 'icons/integral.svg'
      },
      {
        name: 'Euler Functions',
        description: "Returns gamma, beta & phi functions of any number",
        link: 'https://github.com/jralvarenga/mathapi/tree/master/mathapi/math/euler_functions',
        icon: 'icons/euler.svg'
      },
      {
        name: 'Factorial',
        description: "Gets the factorial value of an integer or fraction",
        link: 'https://github.com/jralvarenga/mathapi/tree/master/mathapi/math/factorial',
        icon: 'icons/factorial.svg'
      },
      {
        name: 'Algebra',
        description: "To be added",
        link: '#',
        icon: 'icons/algebra.svg'
      },
      {
        name: 'Geometry',
        description: "To be added",
        link: '#',
        icon: 'icons/geometry.svg'
      },
      {
        name: 'Numerical Methods',
        description: "Solves any problem with any numeric method",
        link: 'https://github.com/jralvarenga/mathapi/tree/master/mathapi/math/methods',
        icon: 'icons/methods.svg'
      }]
    }
  },
  methods: {
    goToDoc(link: string) {
      window.open(link)
    }
  }
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
.feature-container {
  width: 80%;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 30px;
}
.feature-box {
  margin: 20px;
  width: 250px;
  height: 150px;
  padding: 15px;
  box-shadow: 0px 0px 30px 1px rgba(0,0,0,0.1);
  border-radius: 15px;
  cursor: pointer;
  transition: 400ms;
}
.feature-box:hover {
  box-shadow: 0px 0px 30px 1px rgba(0,0,0,0.22);
}
.feat-name {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.feat-icon {
  width: 30px;
  height: 30px;
}
.feat-description {
  font-size: 14px;
  height: 100%;
  display: flex;
  align-items: center;
}
</style>