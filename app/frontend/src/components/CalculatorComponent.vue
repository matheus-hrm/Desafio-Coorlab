<script setup lang="ts">
import { TruckIcon, HandCoinsIcon } from 'lucide-vue-next'
import CityButton from './CityButton.vue'
import DateButton from './DateButton.vue'
import axios from 'axios'
</script>
<script lang="ts">
export default {
  components: {
    CityButton,
    DateButton
  },
  data() {
    return {
      selectedDate: '',
      selectedCity: ''
    }
  },
  methods: {
    updateCity(city: string) {
      this.selectedCity = city
      console.log(this.selectedCity)
    },
    updateDate(date: string) {
      this.selectedDate = date
      console.log(this.selectedDate)
    },
    searchTrip() {
      if (this.selectedCity === "São Paulo"){
        this.selectedCity = "Sao-Paulo"
      }
      axios.get(`http://localhost:8000/${this.selectedCity}`).then((response) => {
        console.log(response.data)
      })
    }
  }
}
</script>

<template>
  <div class="w-full h-full flex flex-col rounded-md drop-shadow-2xl bg-white">
    <div class="bg-slate-800 flex flex-row space-x-4 items-center px-6 py-4 rounded-t-md">
      <TruckIcon class="w-10 h-10 text-white" />
      <h1 class="pl-2 text-white text-2xl">Calculadora de Viagem</h1>
    </div>
    <div class="flex flex-row justify-center py-28 items-center">
      <div class="bg-gray-100 w-1/3 rounded-md">
        <div class="flex flex-col justify-center items-center space-y-5">
          <div class="flex flex-row items-center justify-center mt-8">
            <HandCoinsIcon class="w-10 h-10 text-black" />
            <h1 class="text-2xl ml-4">Calcule o valor da viagem</h1>
          </div>
          <div class="w-full flex flex-col ml-20">
            <h1 class="text-gray-900">Destino</h1>
            <CityButton @update-city="updateCity" />
          </div>

          <div class="w-full flex flex-col ml-20 mt-8">
            <h1 class="text-gray-900">Data</h1>
            <DateButton @update-date="updateDate" />
          </div>

          <div class="w-2/4 m-8 pb-10">
            <button
              class="bg-cyan-500 text-black w-full h-12 rounded-md mt-8"
              type="submit"
              @click="searchTrip"
            >
              Buscar
            </button>
          </div>
        </div>
      </div>
      <div class="flex flex-col justify-center items-center w-1/2 h-full">
        <h1 class="text-3xl">Nenhum dado selecionado</h1>
      </div>
    </div>
  </div>
</template>
