<template>
  <div>
    <label for="username" class="block text-sm/6 font-medium text-gray-900">Username</label>
    <div class="mt-2">
      <input
        id="username"
        type="text"
        autocomplete="username"
        :required="true"
        v-model="modelValue"
        class="block w-full rounded-md px-3 py-1.5 text-gray-900 outline outline-1 outline-gray-300 placeholder:text-gray-400 focus:outline-indigo-600 sm:text-sm/6"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
const modelValue = defineModel({ type: String })
</script>
