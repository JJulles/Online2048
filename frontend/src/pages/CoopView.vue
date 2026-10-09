<template>
  <h1>2048 Coop</h1>
  <div :id="`grid-${pseudo}`">
    <p>Grille de jeu</p>
  </div>
</template>


<script setup>
  import {ref} from 'vue'
  const pseudo = ref("");

</script>