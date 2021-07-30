<template>
  <div>
    <top-bar />

    <div class="try-body">
      <div class="body-request">
        <json-editor :schema="schema"
            :initial-value="body"
            @update-value="updateValue($event)"
            theme="bootstrap3"
            icon="fontawesome4">
        </json-editor>
      </div>
      <div class="body-response"></div>
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
      body: {}
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
}
.body-response {
  width: 50%;
  height: 100%;
}
</style>