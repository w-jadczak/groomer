<template>
  <RouterView v-slot="{ Component }">
    <Suspense>
      <component :is="Component"></component>

      <template #fallback>
        <Loading />
      </template>
    </Suspense>
  </RouterView>
</template>

<script setup lang="ts">
import { RouterView } from "vue-router"
import Loading from "@/common/components/LoadingIndicator.vue"
</script>
