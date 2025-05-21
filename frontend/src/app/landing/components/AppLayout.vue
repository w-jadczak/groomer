<template>
  <AppNav />
  <div class="py-10">
    <header v-if="pageTitle">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <h1 class="text-3xl font-bold tracking-tight text-gray-900">{{ pageTitle }}</h1>
      </div>
    </header>
    <main>
      <div class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <RouterView v-slot="{ Component }">
          <template v-if="Component">
            <KeepAlive>
              <Suspense>
                <component :is="Component"></component>
                <template #fallback>
                  <div class="h-screen flex justify-content-center align-items-center">
                    <LoadingIndicator />
                  </div>
                </template>
              </Suspense>
            </KeepAlive>
          </template>
        </RouterView>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { RouterView } from "vue-router"
import AppNav from "@/app/landing/components/nav-bar/AppNav.vue"
import LoadingIndicator from "@/common/components/LoadingIndicator.vue"
import { useRoute } from "vue-router"
import { computed } from "vue"

const route = useRoute()
const pageTitle = computed(() => route.meta.title as string | undefined)
</script>
