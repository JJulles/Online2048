<template>
  <div class="border rounded-md lg:rounded-4xl">
    <img :src='getImageURL(value)' alt="" class="w-15 sm:w-18 md:w-20 lg:w-25"/>
  </div>
</template>

<script setup>
defineProps({
  value:Number
})

// Calculate the right URL for the image based on the tile's value
const getImageURL = (val) => {
  return new URL(`../assets/${val}.svg`, import.meta.url).href
}
</script>