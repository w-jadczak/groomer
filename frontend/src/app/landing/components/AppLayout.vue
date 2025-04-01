<!-- AppLayout.vue -->
<template>
  <AppNav />
  <RouterView v-slot="{ Component }">
    <template v-if="Component">
      <KeepAlive>
        <Suspense>
          <!-- Main Content -->
          <component :is="Component"></component>
          <!-- Loading State -->
          <template #fallback>
            <div class="h-screen flex justify-content-center align-items-center">
              <LoadingIndicator />
            </div>
          </template>
        </Suspense>
      </KeepAlive>
    </template>
  </RouterView>
  <AppFooter />
</template>

<script setup lang="ts">
import { RouterView } from "vue-router"
import AppNav from "@/common/components/nav-bar/AppNav.vue"
import AppFooter from "@/common/components/AppFooter.vue"
import LoadingIndicator from "@/common/components/LoadingIndicator.vue"
</script>
