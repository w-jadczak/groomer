<script setup lang="ts">
import { Bars3Icon, XMarkIcon } from "@heroicons/vue/24/outline"
import { DisclosureButton } from "@headlessui/vue"
</script>

<template>
  <div class="-mr-2 flex items-center sm:hidden">
    <DisclosureButton
      class="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500"
    >
      <span class="absolute -inset-0.5" />
      <span class="sr-only">Open main menu</span>
      <Bars3Icon v-if="!open" class="block size-6" aria-hidden="true" />
      <XMarkIcon v-else class="block size-6" aria-hidden="true" />
    </DisclosureButton>
  </div>
</template>

<style scoped></style>
