<template>
  <div>
    <top-bar />

    <div class="try-body">
      <div class="body-request">
        <div class="title">
          <span>Try the API</span>
        </div>
        <div class="description">
          <span>Select or write the API url you what to try (Read the <a target="_blank" href="https://github.com/jralvarenga/mathapi">docs</a> first)</span>
        </div>
        <div class="input-container">
          <input class="url-input" type="text" v-model="url">
          <select class="url-select" @change="changeBody">
            <option value="plot">Function plot</option>
            <option value="derivative">Derivative</option>
            <option value="integral">Integral</option>
            <option value="beta">Beta function</option>
            <option value="factorial">Factorial</option>
            <option value="newton-rhapson">Newton Rhapson method</option>
            <option value="trapz-rule">Trapezoidal rule</option>
          </select>
        </div>
        <div class="json-editor">
          <textarea class="json-textarea" v-model="body"></textarea>
          <button class="send-button" @click="getResponse">Send</button>
        </div>
      </div>
      <div class="body-response">
        <textarea class="json-textarea response-json" v-model="response"></textarea>
      </div>
    </div>

  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import TopBar from '../components/TopBar.vue';

export default defineComponent({
  components: { TopBar },
  name: "TryAPI",
  data() {
    return {
      url: "https://mathapi.vercel.app/api/function/points/",
      body: JSON.stringify({"fx": "3*x^(3) + 2*x - 1","from": -1,"to": 5}, undefined, 2),
      response: JSON.stringify({}, undefined, 2)
    }
  },
  methods: {
    // eslint-disable-next-line
    changeBody(e: any) {
      const type: string = e.target.value;
      switch (type) {
        case 'plot':
          this.url = "https://mathapi.vercel.app/api/function/points/";
          this.body = JSON.stringify({"fx": "3*x^(3) + 2*x - 1","from": -1,"to": 5}, undefined, 2);
        break;
        case 'derivative':
          this.url = "https://mathapi.vercel.app/api/derivative/";
          this.body = JSON.stringify({"fx": "3*x^(3) - 2*x^(1/2) + 1"}, undefined, 2);
        break;
        case 'integral':
          this.url = "https://mathapi.vercel.app/api/integral/";
          this.body = JSON.stringify({"fx": "3*x^(3) - 2*x^(1/2) + 1"}, undefined, 2);
        break;
        case 'beta':
          this.url = "https://mathapi.vercel.app/api/euler-functions/beta/";
          this.body = JSON.stringify({"x": "1/2","y": "3"}, undefined, 2);
        break;
        case 'factorial':
          this.url = "https://mathapi.vercel.app/api/factorial/";
          this.body = JSON.stringify({"n": "1/2"}, undefined, 2);
        break;
        case 'newton-rhapson':
          this.url = "https://mathapi.vercel.app/api/numeric-methods/function-root/newton-rhapson/";
          this.body = JSON.stringify({"fx": "2*x^(3)-2*x-5","xi": 2}, undefined, 2);
        break;
        case 'trapz-rule':
          this.url = "https://mathapi.vercel.app/api/numeric-methods/integral/trapz/";
          this.body = JSON.stringify({"fx": "3*x^(2) + 3*x - 1","a": 0,"b": 1}, undefined, 2);
        break;
        default:
          this.url = "https://mathapi.vercel.app/api/function/points/";
          this.body = JSON.stringify({"fx": "3*x^(3) + 2*x - 1","from": -1,"to": 5}, undefined, 2);
        break;
      }      
    },
    async getResponse() {
      const link: string = this.url;
      // eslint-disable-next-line
      const body: any = this.body;
      const res = await fetch(link, {
        method: 'post',
        headers: {
          'Content-Type': "application/json",
        },
        body: body,
        redirect: 'follow'
      });
      const data = await res.json();
      this.response = JSON.stringify(data, undefined, 2);
    }
  }  
})
</script>

<style>
.try-body {
  display: flex;
  align-items: center;
  flex-direction: row;
  justify-content: space-between;
  height: calc(100vh - 80px);
}
.body-request {
  width: 50%;
  height: 100%;
  padding-left: 3%;
}
.body-response {
  width: 50%;
  height: 100%;
  display: flex;
  align-items: flex-end;
}
.title {
  margin-top: 30px;
  font-family: inter-extrabold;
  font-size: 45px;
}
.description {
  margin-top: 30px;
}
.input-container {
  width: 100%;
  margin-top: 30px;
  display: flex;
  flex-direction: row;
  align-items: center;
}
.url-input {
  font-family: inter;
  font-weight: bold;
  color: rgb(56, 56, 56);
  width: 60%;
  padding: 10px;
  border-bottom-left-radius: 20px;
  border-top-left-radius: 20px;
  border: 1px solid gray;
}
.url-select {
  font-family: inter;
  font-weight: bold;
  color: rgb(56, 56, 56);
  width: 20%;
  padding: 9px;
  border-bottom-right-radius: 20px;
  border-top-right-radius: 20px;
  border: 1px solid gray;
}
.json-editor {
  width: 90%;
  height: 50%;
  margin-top: 30px;
  display: flex;
  flex-direction: column;
}
.json-textarea {
  width: 100%;
  height: 70%;
  resize: none;
  border-radius: 20px;
  padding: 10px;
}
.response-json {
  width: 90%;
  height: 70%;
  margin-bottom: 50px;
}
.json-textarea:focus {
  outline: none;
}
.send-button {
  width: 100px;
  padding: 10px;
  margin-top: 20px;
  background: rgb(59, 46, 131);
  color: #fff;
  font-family: inter-extrabold;
  border-radius: 10px;
  border: 0px;
  cursor: pointer;
  transition: 300ms;
}
.send-button:hover {
  background: rgb(47, 37, 104);
  transition: 100ms;
}
.send-button:active {
  background: rgb(82, 65, 182);
}
</style>