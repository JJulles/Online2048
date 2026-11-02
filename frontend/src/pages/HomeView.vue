<template>
  <!-- Flowbite component -->
  <fwb-jumbotron
    header-text="2048 Online"
    sub-text="On a tous déjà rêvé de jouer à un 2048 avec ses ami·e·s non ? Non ? Qu'importe, maintenant que tu es là, viens jouer !"
    class="mt-30 opacity-90 backdrop-blur-xl"
  >
    <!-- Buttons -->
    <div class="flex flex-col space-y-4 sm:flex-row sm:justify-center sm:space-y-0">
      <RouterLink to="solo"
                  class="inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-white rounded-lg bg-512
                  hover:bg-4096 focus:ring-4 dark:focus:ring-blue-900">
        Jouer seul
      </RouterLink>

      <RouterLink to="coop"
                  class="inline-flex justify-center items-center py-3 px-5 sm:ml-4 text-base font-medium text-center text-gray-900 rounded-lg border border-gray-300
        hover:bg-2 focus:ring-gray-100 dark:text-white dark:border-gray-700 dark:hover:bg-gray-700 dark:focus:ring-gray-800">
        Jouer en ligne
      </RouterLink>
    </div>
  </fwb-jumbotron>

  <BackgroundEffect amount-decoration="50" duration="5"/>
</template>

<script setup>
  import { FwbJumbotron } from 'flowbite-vue'
  import {RouterLink} from "vue-router";
  import BackgroundEffect from "@/components/BackgroundEffect.vue";
</script>