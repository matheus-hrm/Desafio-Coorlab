<script setup lang="ts">
import { ref, watch } from 'vue'
const date = ref(null)

const emit = defineEmits(['updateDate'])
watch(() => date.value, (date) => {
  emit('updateDate', date)
})
</script>

<template>
  <div class="flex flex-row">
    <input
      type="date"
      v-model="date"
      class="w-3/4 h-12 rounded-md border-2 border-gray-300 pl-3 pr-3 shadow-md focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent"
      placeholder="Selecione a data da viagem"
      @change="$emit('updateDate', date)"    />
  </div>
</template>

<style scoped>
input[type='date']::-webkit-inner-spin-button,
input[type='date']::-webkit-calendar-picker-indicator {
  margin: 0;
}
input[type='date']::-webkit-input-placeholder {
  color: gray;
  font-size: 0.875rem;
}
</style>
