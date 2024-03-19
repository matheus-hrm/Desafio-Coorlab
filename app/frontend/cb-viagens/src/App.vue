<script setup lang="ts">
import { Calculator } from 'lucide-vue-next';
import CalculatorComponent from './components/CalculatorComponent.vue';

</script>

<template>
  <div class="flex flex-row w-screen h-screen">
    <div class="flex flex-col bg-gray-800 w-1/4 h-full">
      <div class="flex justify-center items-center">
        <img class="mt-8" src="@/assets/logo.png" width="250" height="250" />
      </div>
      <div class="mt-12 flex flex-row justify-center space-x-3">
        <Calculator class="text-white w-8 h-8" />
        <h1 class="text-white text-2xl flex justify-center">Calculadora de Viagens</h1>
      </div>
    </div>
    <div class="flex flex-col h-full w-screen bg-slate-50">
      <div class="shadow-lg h-28 bg-white"></div>
      <div class="flex mx-12 my-16 ">
        <CalculatorComponent />
      </div>
    </div>
  </div>
</template>
