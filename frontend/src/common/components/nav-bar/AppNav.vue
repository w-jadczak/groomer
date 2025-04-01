<template>
  <Disclosure as="nav" class="bg-white shadow w-full fixed top-0 left-0 z-50">
    <div class="mx-auto max-w-full px-4 sm:px-6 lg:px-8">
      <div class="flex h-16 justify-between">
        <div class="flex">
          <div class="flex shrink-0 items-center">
            <img
              class="h-8 w-auto"
              src="https://tailwindcss.com/plus-assets/img/logos/mark.svg?color=indigo&shade=600"
              alt="Your Company"
            />
          </div>
          <DesktopMenu />
        </div>
        <UserMenu />
        <MobileMenu />
      </div>
    </div>
  </Disclosure>
</template>

<script setup lang="ts">
import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
} from "@headlessui/vue"
import { Bars3Icon, BellIcon, XMarkIcon } from "@heroicons/vue/24/outline"
import MobileMenu from "@/common/components/nav-bar/MobileMenu.vue"
import DesktopMenu from "@/common/components/nav-bar/DesktopMenu.vue"
import UserMenu from "@/common/components/nav-bar/UserMenu.vue"
</script>
