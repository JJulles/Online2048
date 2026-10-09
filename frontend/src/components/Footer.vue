<template>
  <fwb-footer footer-type="logo" class="absolute bottom-0 w-full opacity-90 backdrop-blur-sm">
    <div class="w-full max-w-(--breakpoint-xl) mx-auto p-4 md:py-8">
      <div class="sm:flex sm:items-center sm:justify-between">
        <fwb-footer-brand src="logo.svg" alt="2048 Online Logo" name="2048 Online" />
        <fwb-footer-link-group class="flex flex-wrap items-center mb-6 gap-5 text-sm text-gray-500 sm:mb-0 dark:text-gray-400">
          <RouterLink to="/about">
            A propos
          </RouterLink>
          <RouterLink to="/contact">
            Contact
          </RouterLink>
        </fwb-footer-link-group>
      </div>
      <fwb-footer-copyright href="/" by="Jules Couture™" />
    </div>
  </fwb-footer>
</template>

<script setup>
import {
  FwbFooter,
  FwbFooterBrand,
  FwbFooterCopyright,
  FwbFooterLinkGroup,
} from 'flowbite-vue'
</script>