<template>
  <BaseModal v-model:is-open="isOpen">sdfdfdf </BaseModal>
</template>

<script setup lang="ts">
import BaseModal from "@/common/components/base-modal/BaseModal.vue"

const isOpen = defineModel("is-open", { type: Boolean, default: false })
</script>

<style scoped></style>
