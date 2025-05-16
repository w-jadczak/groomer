<template>
  <button
    type="submit"
    class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
  >
    {{ label }}
  </button>
</template>
<script setup lang="ts">
const props = defineProps({
  type: { type: String, default: "submit" },
  label: { type: String, required: true },
})
</script>

<style scoped></style>
