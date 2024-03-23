<script setup lang="ts">
import { TruckIcon, HandCoinsIcon, ClockIcon, AlertTriangleIcon } from 'lucide-vue-next'
import CityButton from './CityButton.vue'
import DateButton from './DateButton.vue'
import axios from 'axios'
import { ref } from 'vue'

interface Trips {
  cheapest_route: cheapestTrip
  fastest_route: fastestTrip
}

interface cheapestTrip {
  name: string
  seat: number
  duration: string
  price_econ: number
}

interface fastestTrip {
  name: string
  bed: number
  duration: string
  price_confort: number
}

const selectedCity = ref('')
const selectedDate = ref('')
const tripsData = ref<Trips[]>([])
const cheapestTripData = ref<cheapestTrip | null>()
const fastestTripData = ref<fastestTrip | null>()
const showModal = ref(false)

const updateCity = (city: string) => {
  selectedCity.value = city
}

const updateDate = (date: string) => {
  selectedDate.value = date
}

const emptyData = () => {
  cheapestTripData.value = null
  fastestTripData.value = null
}

const searchTrip = () => {
  if (selectedCity.value === '' || selectedDate.value === '') {
    showModal.value = true
    return
  }
  axios.get(`http://localhost:3000/${selectedCity.value}`).then((response) => {
    const data = response.data
    tripsData.value = data
    cheapestTripData.value = data.cheapest_route
    fastestTripData.value = data.fastest_route
    console.log(data)
  })
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
              class="bg-cyan-500 text-black w-full h-12 rounded-md mt-8 drop-shadow-2xl hover:bg-sky-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500"
              type="submit"
              @click="searchTrip"
            >
              Buscar
            </button>
          </div>
        </div>
      </div>
      <div class="flex flex-col justify-center items-center w-1/2 h-full">
        <h1 v-if="!cheapestTripData && !fastestTripData" class="text-3xl ml-8">
          Nenhum dado selecionado
        </h1>
        <div v-else>
          <h1 class="text-2xl ml-4 text-center">
            Essas são as melhores alternativas de viagem para a data selecionada
          </h1>
          <div
            v-if="fastestTripData && fastestTripData.name"
            class="flex flex-row justify-center mt-4"
          >
            <div class="px-8 bg-teal-600 rounded-l-lg flex flex-col justify-center">
              <ClockIcon class="w-10 h-10 text-white" />
            </div>
            <div class="flex flex-col justify-center items-center bg-gray-100 py-4 px-12 w-72">
              <h1 class="text-xl font-semibold">{{ fastestTripData.name }}</h1>
              <h1 class="text-md">Leito: {{ fastestTripData.bed }}</h1>
              <h1 class="text-md">Tempo Estimado: {{ fastestTripData.duration }}</h1>
            </div>
            <div
              class="flex flex-col justify-center items-center ml-2 bg-gray-100 rounded-md p-8 w-48"
            >
              <h1 class="font-medium text-lg">Preço</h1>
              <h1 class="text-lg mt-2">{{ fastestTripData.price_confort }}</h1>
            </div>
          </div>
          <div v-if="cheapestTripData" class="flex flex-row justify-center mt-4">
            <div class="px-8 bg-cyan-500 rounded-l-lg flex flex-col justify-center">
              <HandCoinsIcon class="w-10 h-10 text-white" />
            </div>
            <div class="flex flex-col justify-center items-center bg-gray-100 py-4 px-12 w-72">
              <h1 class="text-xl font-semibold">{{ cheapestTripData.name }}</h1>
              <h1 class="text-md">Poltrona: {{ cheapestTripData.seat }}</h1>
              <h1 class="text-md">Tempo Estimado: {{ cheapestTripData.duration }}</h1>
            </div>
            <div
              class="flex flex-col justify-center items-center ml-2 bg-gray-100 rounded-md p-8 w-48"
            >
              <h1 class="font-medium text-lg">Preço</h1>
              <h1 class="text-lg mt-2">{{ cheapestTripData.price_econ }}</h1>
            </div>
          </div>
          <div class="flex flex-row justify-end">
            <div class="flex flex-row justify-end w-full">
              <button
                class="bg-yellow-500 text-black w-2/4 h-12 rounded-md mt-8 hover:bg-yellow-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500"
                @click="emptyData"
              >
                Limpar
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    v-if="showModal"
    class="fixed z-0 inset-0 flex items-center justify-center shadow-2xl drop-shadow-2xl"
    aria-labelledby="modal-title"
    role="dialog"
    aria-modal="true"
  >
    <div
      class="bg-white rounded-lg px-4 pt-5 pb-4 sm:p-6 sm:pb-4 flex flex-col justify-center items-center"
    >
      <AlertTriangleIcon class="w-10 h-10 text-yellow-500" />
      <h3 class="text-lg leading-6 font-medium text-gray-900" id="modal-title">Atenção</h3>
      <div class="mt-2">
        <p class="text-md text-gray-500 text-center">Por favor, selecione uma cidade e uma data</p>
      </div>
      <div class="mt-5 sm:mt-6">
        <button
          type="button"
          @click="showModal = false"
          class="inline-flex justify-center w-full rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:text-sm"
        >
          Fechar
        </button>
      </div>
    </div>
  </div>
</template>
