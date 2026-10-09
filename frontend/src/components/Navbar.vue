<template>
  <div class="border-b rounded-b-xl border-b-gray-600 backdrop-blur-sm opacity-90
  dark:bg-gray-800 dark:text-white">
    <div class="flex justify-between items-center mx-5 sm:mx-20 py-3">
      <div >
        <RouterLink to="/" class="flex items-center space-x-4">
          <img src="/logo.svg" alt="" class="w-12" />
          <span>Accueil</span>
        </RouterLink>
      </div>

      <div>
        <RouterLink
            v-for="item in ['Solo','Coop','About']" :to="item.toLowerCase()"
            class="mx-3 hover:dark:bg-gray-900"
        >
          {{item}}
        </RouterLink>
      </div>

    </div>
  </div>

</template>

<script setup>
  import { RouterLink } from 'vue-router'
</script>
