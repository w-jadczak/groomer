<script setup lang="ts">
import { MenuButton, MenuItem, MenuItems, Menu } from "@headlessui/vue"
import { useAuthStore } from "@/common/stores/useAuthStore.ts"
import { storeToRefs } from "pinia"
import { ArrowRightCircleIcon } from "@heroicons/vue/20/solid"

const { isAuthenticated } = storeToRefs(useAuthStore())
</script>

<template>
  <Menu as="div" class="relative ml-3 flex items-center">
    <div>
      <MenuButton
        v-if="isAuthenticated"
        class="relative flex rounded-full bg-white text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
      >
        <span class="absolute -inset-1.5" />
        <span class="sr-only">Open user menu</span>
        <img
          class="size-8 rounded-full"
          src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
          alt=""
        />
      </MenuButton>
      <button
        v-else
        class="relative flex rounded-full bg-white text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
      >
        <ArrowRightCircleIcon class="h-10 w-10 text-indigo-500" />
      </button>
    </div>
    <transition
      enter-active-class="transition ease-out duration-200"
      enter-from-class="transform opacity-0 scale-95"
      enter-to-class="transform opacity-100 scale-100"
      leave-active-class="transition ease-in duration-75"
      leave-from-class="transform opacity-100 scale-100"
      leave-to-class="transform opacity-0 scale-95"
    >
      <MenuItems
        class="absolute right-0 top-full mt-0 z-10 w-48 rounded-md bg-white py-1 shadow-lg ring-1 ring-black/5"
      >
        <MenuItem v-slot="{ active }">
          <a
            href="#"
            :class="[
              active ? 'bg-gray-100 outline-none' : '',
              'block px-4 py-2 text-sm text-gray-700',
            ]"
            >Your Profile</a
          >
        </MenuItem>
        <MenuItem class="flex" v-slot="{ active }">
          <a
            href="#"
            :class="[
              active ? 'bg-gray-100 outline-none' : '',
              'block px-4 py-2 text-sm text-gray-700',
            ]"
            >Settings</a
          >
        </MenuItem>
        <MenuItem v-slot="{ active }">
          <a
            href="#"
            :class="[
              active ? 'bg-gray-100 outline-none' : '',
              'block px-4 py-2 text-sm text-gray-700',
            ]"
            >Sign out</a
          >
        </MenuItem>
      </MenuItems>
    </transition>
  </Menu>
</template>

<style scoped></style>
