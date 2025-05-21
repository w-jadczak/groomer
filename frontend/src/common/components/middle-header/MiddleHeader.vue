<template>
  <div class="sm:mx-auto sm:w-full sm:max-w-sm">
    <img
      class="mx-auto h-10 w-auto"
      src="https://tailwindcss.com/plus-assets/img/logos/mark.svg?color=indigo&shade=600"
      alt="Your Company"
    />
    <h2 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">
      {{ title }}
    </h2>
  </div>
</template>

<script setup lang="ts">
const props = defineProps({
  title: { type: String, required: true },
})
</script>

<style scoped></style>
