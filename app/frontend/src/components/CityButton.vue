<script setup lang="ts">
import { ref, watch } from 'vue'

const selectedCity = ref('')

const cities = [
  { name: 'Curitiba' },
  { name: 'São Paulo' },
  { name: 'Rio de Janeiro' },
  { name: 'Belo Horizonte' },
  { name: 'Fortaleza' },
  { name: 'Salvador' },
  { name: 'Campinas' },
  { name: 'Natal' },
  { name: 'Manaus' },
  { name: 'Recife' }
]

const emit = defineEmits(['updateCity'])

watch(() => selectedCity.value, (city) => {
  emit('updateCity', city)
})

</script>

<template>
  <div class="flex flex-col md:flex-row">
    <select
      v-model="selectedCity"
      class="w-full md:w-3/4 h-12 rounded-md border-2 border-gray-300 pl-3 pr-3 shadow-md focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent"
      @change="$emit('updateCity', selectedCity)"
    >
      <option
        v-for="city in cities"
        :key="city.name"
        :value="city.name"
        class="w-full md:w-3/4 h-12 rounded-md border-2 border-gray-300 pl-3 pr-3 shadow-md focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent"
      >
        {{ city.name }}
      </option>
    </select>
  </div>
</template>
