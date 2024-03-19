<script setup lang="ts">
import { TruckIcon, HandCoinsIcon, ChevronRightIcon, CalendarDaysIcon } from 'lucide-vue-next'
</script>

<template>
  <div class="w-full h-full flex flex-col rounded-md drop-shadow-2xl bg-white">
          <div class="bg-slate-800 flex flex-row space-x-4 items-center px-6 py-4 rounded-t-md" >
            <TruckIcon class="w-10 h-10 text-white" /> 
            <h1 class="pl-2 text-white text-2xl">Calculadora de Viagem</h1>
          </div>
          <div class="flex flex-row justify-center py-28 items-center ">
            <div class="bg-gray-100 w-1/3 rounded-md">
              <div class="flex flex-col justify-center items-center space-y-5 ">
                <div class="flex flex-row items-center justify-center mt-8">
                  <HandCoinsIcon class="w-10 h-10 text-black" />
                  <h1 class="text-2xl p-6">
                    Calcule o valor da viagem
                  </h1>
                </div>
                <div class="w-full flex flex-col ml-20">
                  <h1 class="text-gray-900">Destino</h1>
                  <button class="bg-white flex items-center justify-between border border-gray-300 w-3/4 h-12 rounded-md place-content-start">
                    <h1 class="text-gray-600 ml-4">Selecione o destino</h1>
                    <ChevronRightIcon class="w-8 mr-2 text-gray-500" />
                  </button>
                </div>

                <div class="w-full flex flex-col ml-20 mt-8">
                  <h1 class="text-gray-900">Data</h1>
                  <button class="bg-white flex items-center justify-between border border-gray-300 w-3/4 h-12 rounded-md place-content-start">
                    <h1 class="text-gray-600 ml-4">Selecione uma data</h1>
                    <CalendarDaysIcon class="w-8 mr-2 text-gray-500" />
                  </button>
                </div>

                <div class="w-2/4 m-8 pb-10">
                  <button class="bg-cyan-500 text-black w-full h-12 rounded-md mt-8">Buscar</button>
                </div>
              </div>
            </div>
            <div class="flex flex-col justify-center items-center w-1/2 h-full">
              <h1 class="text-3xl ">Nenhum dado selecionado</h1>
            </div>
          </div>
        </div>
</template>

