<template>
  <div class="flex flex-row gap-10">
    <!-- First col - Pseudo -->
    <div>
      <span class="text-center font-bold text-xl dark:text-white">Pseudonyme</span>
      <div v-if="leaderboard.length>0">
        <template v-for="row in leaderboard">
          <p>{{row.at(0)}}</p>
        </template>
      </div>
      <div v-else>
        <p class="italic text-gray-400 text-sm">Aucune valeur</p>
      </div>
    </div>

    <!-- Second col - Score -->
    <div class="">
      <span class="text-center font-bold text-xl dark:text-white">Score</span>
      <div v-if="leaderboard.length>0">
        <template v-for="row in leaderboard">
          <p>{{row.at(1)}}</p>
        </template>
      </div>
      <div v-else>
        <p class="italic text-gray-400 text-sm">Aucune valeur</p>
      </div>
    </div>

  </div>
</template>

<script setup>

defineProps({
  leaderboard: Array
})

</script>