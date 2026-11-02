<template>
  <div class="flex justify-center">
    <div class="grid grid-cols-4 gap-2">
      <template v-for="(row, rowIndex) in grid.values()">
        <Tile v-for="(value, colIndex) in row" :key="`${rowIndex}-${colIndex}`" :value="value"/>
      </template>
    </div>
  </div>

</template>

<script setup>
  import Tile from "@/components/Tile.vue";

  defineProps({
    grid: Array
  })
</script>
